import os

import allure
from allure_commons.types import Severity
from selene import have
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from pages.issues_page import Issue
from tests.confest import browser_setup


# def test_github_by_selene(browser_setup):
#     browser.open('https://github.com')
#     s('.search-input').click()
#     s('#query-builder-test').send_keys('87stels87/qa_guru_hw1').press_enter()
#     s(by.link_text('87stels87/qa_guru_hw1')).click()
#     s('#issues-tab').click()
#     s(by.css(".blankslate-heading")).should(have.exact_text('No results'))
#
#
# def test_github_with_allure_step(browser_setup):
#     with allure.step("Открываем главную страницу гитхаб"):
#         browser.open('https://github.com')
#     with allure.step("Ищем репозиторий"):
#         s('.search-input').click()
#         s('#query-builder-test').send_keys('87stels87/qa_guru_hw1').press_enter()
#     with allure.step("Переходим по найденному репозиторию"):
#         s(by.link_text('87stels87/qa_guru_hw1')).click()
#     with allure.step("Переходим по вкладку issues"):
#         s('#issues-tab').click()
#     with allure.step("Проверяем что открытых issues нет"):
#         s(by.css(".blankslate-heading")).should(have.exact_text('No results'))
#
#
# @allure.feature("Проверка отображения issues в репозитории")
# @allure.epic("Гитхаб")
# @allure.tag("smoke")
# @allure.severity(Severity.NORMAL)
# @allure.link("https://github.com", name="issue text")
# @allure.step("Поиск issues по тексту элемента")
# @allure.label("owner", "Okatev")
# def test_github_with_decorator(browser_setup):
#     issue = Issue()
#     issue.open_main_page()
#     issue.search_repo()
#     issue.go_to_repo()
#     issue.go_to_issues()
#     issue.check_issues()

def test_filling_all_fields(browser_setup):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.maximize_window()
    browser.element('#firstName').click().type("Иван")
    browser.element('#lastName').click().type("Иванов")
    browser.element('#userEmail').click().type("ivanov@ya.ru")
    browser.element('[value=Female]').double_click()
    browser.element('[id="userNumber"]').click().type("1234567890")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="2"]').click()
    browser.element('option[value="2000"]').click()
    browser.element('[aria-label = "Choose Thursday, March 2nd, 2000"]').click()
    browser.element('#subjectsInput').double_click().set("accounting")
    browser.element('#react-select-2-option-0').with_(timeout=browser.config.timeout * 2).double_click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('tests/picture.jpeg'))
    browser.element('[placeholder="Current Address"]').click().type("Москва")
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('table').all('tr').should(have.exact_texts(
        'Label Values',
        'Student Name Иван Иванов',
        'Student Email ivanov@ya.ru',
        'Gender Female',
        'Mobile 1234567890',
        'Date of Birth 02 March,2000',
        'Subjects Accounting',
        'Hobbies Reading',
        'Picture picture.jpeg',
        'Address Москва',
        'State and City NCR Delhi')
    )
