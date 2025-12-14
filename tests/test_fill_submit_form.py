import os
from datetime import date
import allure
from qa_guru_homework_12.registration_steps import RegistrationSteps
from qa_guru_homework_12.user import User


@allure.title("Проверка регистрации пользователя")
@allure.epic("DEMOQA")
@allure.feature("Форма регистрации")
def test_fill_submit_form(setup_browser):
    student = User(
        first_name='Alex',
        last_name='Bagel',
        email='alexbagel@mail.ru',
        gender='Male',
        mobile_number='9021778990',
        date_of_birth=date(1990, 6, 19),
        subject='English',
        hobbies='Sports',
        picture=os.path.join(os.path.dirname(os.path.dirname(__file__)),'mount.jpg'),
        street_address='Lomonosov str. 8',
        state_address='Haryana',
        city_address='Panipat'
    )

    browser = setup_browser
    registration_steps = RegistrationSteps(browser)

    registration_steps.open()
    registration_steps.register(student)
    registration_steps.should_have_registered(student)
