

from sqlalchemy import create_engine, text

db_connection_string = 'postgresql://postgres:svetok@localhost:5432/QA'

db = create_engine(db_connection_string)


def test_add_user():
    """Тест на добавление пользователя и проверку, что он добавился."""
    test_email = "testuser@example.com"
    test_subject_id = 1
    test_name = "Nik"

    with db.connect() as connection:
        # Добавляем тестового пользователя
        connection.execute(
            text("INSERT INTO users (user_email, subject_id, user_name)"
                 " VALUES (:user_email, :subject_id, :user_name)"),
            {"user_email": test_email,
             "subject_id": test_subject_id, "user_name": test_name}
        )
        connection.commit()

        # Проверяем, что пользователь добавился по email
        result = connection.execute(
            text("SELECT user_email, subject_id, user_name"
                 " FROM users WHERE user_email = :email"),
            {"email": test_email}
        )

        # Извлекаем одну строку
        user = result.fetchone()

        # Проверяем, что запись существует
        assert user is not None, (f"Пользователь с email {test_email}"
                                  f" не найден в базе данных")

        # Проверяем соответствие всех полей
        assert user.user_email == test_email
        assert user.subject_id == test_subject_id
        assert user.user_name == test_name

        # Опционально: удаляем пользователя после теста (Cleanup)
        connection.execute(
            text("DELETE FROM users WHERE user_email = :email"),
            {"email": test_email}
        )
        connection.commit()


def test_update_user_email():
    """Тест на добавление пользователя,
    изменение его email и проверку изменений."""
    test_email = "testuser@example.com"
    new_email = "updated_user@example.com"
    test_subject_id = 1
    test_name = "Nik"

    with (db.connect() as connection):
        # 1. Подготовка: Добавляем тестового пользователя
        connection.execute(
            text("INSERT INTO users (user_email, subject_id, user_name)"
                 " VALUES (:user_email, :subject_id, :user_name)"),
            {"user_email": test_email,
             "subject_id": test_subject_id, "user_name": test_name}
        )
        connection.commit()

        # 2. Действие: Изменяем email пользователя
        connection.execute(
            text("UPDATE users SET user_email = :new_email"
                 " WHERE user_email = :old_email"),
            {"new_email": new_email, "old_email": test_email}
        )
        connection.commit()

        # 3. Проверка: Выбираем пользователя по новому email
        result = connection.execute(
            text("SELECT user_email, user_name"
                 " FROM users WHERE user_email = :email"),
            {"email": new_email}
        ).fetchone()

        # Проверяем, что запись найдена
        assert result is not None, (f"Пользователь с email {new_email}"
                                    f" не найден")

        # Проверяем, что email действительно изменился, а имя осталось прежним
        assert result[0] == new_email
        assert result[1] == test_name

        # 4. Проверка: Убеждаемся, что старого email больше нет в базе
        old_result = connection.execute(
            text("SELECT * FROM users WHERE user_email = :email"),
            {"email": test_email}
        ).fetchone()
        assert old_result is None, ("Старый email"
                                    " всё еще существует в базе данных")

        # Очистка данных (опционально)
        connection.execute(text("DELETE FROM users"
                                " WHERE user_email = :email"),
                           {"email": new_email})
        connection.commit()


def test_delete_user():
    """Тест на удаление пользователя и проверку его отсутствия в базе."""
    test_email = "delete_me@example.com"
    test_subject_id = 1
    test_name = "To Be Deleted"

    with db.connect() as connection:
        # 1. Предварительно создаем пользователя, которого будем удалять
        connection.execute(
            text("INSERT INTO users (user_email, subject_id, user_name)"
                 " VALUES (:user_email, :subject_id, :user_name)"),
            {"user_email": test_email,
             "subject_id": test_subject_id, "user_name": test_name}
        )
        connection.commit()

        # 2. Выполняем удаление пользователя
        connection.execute(
            text("DELETE FROM users WHERE user_email = :email"),
            {"email": test_email}
        )
        connection.commit()

        # 3. Проверка: Пытаемся найти пользователя после удаления
        result = connection.execute(
            text("SELECT * FROM users WHERE user_email = :email"),
            {"email": test_email}
        )

        user = result.fetchone()

        # Проверяем, что запись отсутствует (результат запроса пуст)
        assert user is None, (f"Пользователь с email {test_email} "
                              f"все еще существует"
                              f" в базе данных после удаления")
