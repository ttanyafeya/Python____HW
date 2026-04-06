import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
# URL подключения к вашей базе данных
db_connection_string = 'postgresql://postgres:svetok@localhost:5432/QA'

db = create_engine(db_connection_string)

SessionLocal = sessionmaker(bind=db)
Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, nullable=False)
    user_email = Column(String)

@pytest.fixture
def db_session():
    """Фикстура для создания чистой сессии на каждый тест"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture(scope="module")
def db_engine():
    """Создает движок SQLAlchemy для подключения к БД."""
    engine = create_engine(db_connection_string)
    yield engine
    engine.dispose()


def test_get_column_names(db_engine):
    """Тест проверяет подключение и получает список названий колонок таблицы 'users'."""
    table_name = "users"

    # Создаем инспектор для анализа структуры БД
    inspector = inspect(db_engine)

    # Проверяем существование таблицы перед получением колонок
    tables = inspector.get_table_names()
    assert table_name in tables, f"Таблица '{table_name}' не найдена в базе данных"

    # Получаем информацию о колонках
    columns_info = inspector.get_columns(table_name)

    # Извлекаем только названия колонок (ключ 'name' в словаре каждой колонки)
    column_names = [column['name'] for column in columns_info]

    # Выводим названия колонок в консоль (нужен флаг -s при запуске pytest)
    print(f"\nКолонки таблицы {table_name}: {column_names}")

    # Проверки (Assertions)
    assert len(column_names) > 0, f"Таблица '{table_name}' пуста или не имеет колонок"
    assert "user_id" in column_names, "Колонка 'user_id' отсутствует"
    assert "user_email" in column_names, "Колонка 'user_email' отсутствует"
    assert "subject_id" in column_names, "Колонка 'subject_id' отсутствует"

def test_user_crud_operations(db_session):
    # Данные для теста
    test_username = "automation_pioneer"
    updated_email = "new_email@example.com"

    # 1. ДОБАВЛЕНИЕ (CREATE)
    new_user = Users(user_name=test_username, user_email="initial@example.com")
    db_session.add(new_user)
    db_session.commit()

    # Проверка: пользователь появился в БД и получил ID
    fetched_user = db_session.query(Users).filter_by(user_name=test_username).first()
    assert fetched_user is not None
    assert fetched_user.user_name == test_username

    # 2. ИЗМЕНЕНИЕ (UPDATE)
    fetched_user.user_email = updated_email
    db_session.commit()

    # Проверка: изменения сохранились
    db_session.refresh(fetched_user)
    assert fetched_user.user_email == updated_email

    # 3. УДАЛЕНИЕ (DELETE)
    db_session.delete(fetched_user)
    db_session.commit()

    # Проверка: пользователя больше нет в базе
    deleted_user = db_session.query(Users).filter_by(user_name=test_username).first()
    assert deleted_user is None