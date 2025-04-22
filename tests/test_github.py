import allure
from allure_commons.types import Severity
from selene import have
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from pages.issues_page import Issue
from tests.confest import browser_setup


def test_github_by_selene(browser_setup):
    browser.open('https://github.com')
    s('.search-input').click()
    s('#query-builder-test').send_keys('87stels87/qa_guru_hw1').press_enter()
    s(by.link_text('87stels87/qa_guru_hw1')).click()
    s('#issues-tab').click()
    s(by.css(".blankslate-heading")).should(have.exact_text('No results'))


def test_github_with_allure_step(browser_setup):
    with allure.step("Открываем главную страницу гитхаб"):
        browser.open('https://github.com')
    with allure.step("Ищем репозиторий"):
        s('.search-input').click()
        s('#query-builder-test').send_keys('87stels87/qa_guru_hw1').press_enter()
    with allure.step("Переходим по найденному репозиторию"):
        s(by.link_text('87stels87/qa_guru_hw1')).click()
    with allure.step("Переходим по вкладку issues"):
        s('#issues-tab').click()
    with allure.step("Проверяем что открытых issues нет"):
        s(by.css(".blankslate-heading")).should(have.exact_text('No results'))


@allure.feature("Проверка отображения issues в репозитории")
@allure.epic("Гитхаб")
@allure.label("owner", "RS")
@allure.tag("smoke")
@allure.severity(Severity.NORMAL)
@allure.link("https://github.com", name="issue text")
@allure.step("Поиск issues по тексту элемента")
@allure.label("owner", "Okatev")
def test_github_with_decorator(browser_setup):
    issue = Issue()
    issue.open_main_page()
    issue.search_repo()
    issue.go_to_repo()
    issue.go_to_issues()
    issue.check_issues()
