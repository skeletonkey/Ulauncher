import mock
import pytest
from ulauncher.search.apps.AppResultItem import AppResultItem
from ulauncher.search.apps.AppQueryDb import AppQueryDb
from ulauncher.ext.Query import Query


class TestAppResultItem:

    @pytest.fixture
    def item(self, app_queries):
        return AppResultItem({
            'name': 'TestAppResultItem',
            'description': 'Description of TestAppResultItem',
            'icon': 'icon123',
            'desktop_file': 'path/to/desktop_file.desktop'
        })

    @pytest.fixture
    def app_queries(self, mocker):
        get_instance = mocker.patch('ulauncher.search.apps.AppResultItem.AppQueryDb.get_instance')
        get_instance.return_value = mock.create_autospec(AppQueryDb)
        return get_instance.return_value

    def test_get_name(self, item):
        assert item.get_name() == 'TestAppResultItem'

    def test_get_description(self, item):
        assert item.get_description(Query('q')) == 'Description of TestAppResultItem'

    def test_get_icon(self, item):
        assert item.get_icon() == 'icon123'

    def test_selected_by_default(self, item, app_queries):
        app_queries.find.return_value = 'TestAppResultItem'
        assert item.selected_by_default('q')
        app_queries.find.assert_called_with('q')

    def test_on_enter(self, item, mocker, app_queries):
        LaunchAppAction = mocker.patch('ulauncher.search.apps.AppResultItem.LaunchAppAction')
        ActionList = mocker.patch('ulauncher.search.apps.AppResultItem.ActionList')
        assert item.on_enter(Query('query')) is ActionList.return_value
        LaunchAppAction.assert_called_with('path/to/desktop_file.desktop')
        ActionList.assert_called_with((LaunchAppAction.return_value,))
        app_queries.put.assert_called_with('query', 'TestAppResultItem')
        app_queries.commit.assert_called_with()
