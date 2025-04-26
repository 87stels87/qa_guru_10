import allure
from selene import have
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from tests.confest import browser_setup


def test_github_with_allure_step(browser_setup):
    # browser.open('https://ya.ru')
    with allure.step("Открываем главную страницу гитхаб"):
        browser.open('https://github.com')
    # with allure.step("Ищем репозиторий"):
    #     s('.search-input').with_(timeout=browser.config.timeout * 3).click()
    #     s('#query-builder-test').send_keys('87stels87/qa_guru_hw1').press_enter()
    # with allure.step("Переходим по найденному репозиторию"):
    #     s(by.link_text('87stels87/qa_guru_hw1')).click()
    # with allure.step("Переходим по вкладку issues"):
    #     s('#issues-tab').click()
    # with allure.step("Проверяем что открытых issues нет"):
    #     s(by.css(".blankslate-heading")).should(have.exact_text('No results'))
