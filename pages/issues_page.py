import allure
from selene import browser, by, have
from selene.support.shared.jquery_style import s


class Issue:
    @allure.step('Открываем главную страницу Гитхаб')
    def open_main_page(self):
        browser.open("https://github.com")

    @allure.step('Ищем репозиторий')
    def search_repo(self):
        s('.search-input').click()
        s('#query-builder-test').send_keys('87stels87/qa_guru_hw1').press_enter()

    @allure.step('Переходим по найденному репозиторию')
    def go_to_repo(self):
        s(by.link_text('87stels87/qa_guru_hw1')).click()

    @allure.step('Переходим по вкладку issues')
    def go_to_issues(self):
        s('#issues-tab').click()

    @allure.step('Проверяем что открытых issues нет')
    def check_issues(self):
        s(by.css(".blankslate-heading")).should(have.exact_text('No results'))


