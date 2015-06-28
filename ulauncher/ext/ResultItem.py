class ResultItem(object):

    ICON_SIZE = 40
    UI_FILE = 'result_item'

    score = None  # used by SortedResultList class to maintain sorted by score order of items

    def get_keyword(self):
        """
        If keyword is defined, search will be performed by keyword, otherwise by name.
        """

    def get_name(self):
        raise RuntimeError("%s#get_name() is not implemented" % self.__class__.__name__)

    def get_description(self, query):
        """
        optional
        """

    def get_icon(self):
        """
        optional
        Gtk.PixBuf
        """

    def include_in_results(self):
        """
        Return True to display item among apps in the default search
        """
        return True

    def selected_by_default(self, query):
        """
        Return True if item should be selected by default
        """
        return False

    def on_enter(self, query):
        """
        :param str argument: it is passed only if get_keyword() is implemented
        This allows you to create flows with a result item
        Return ActionList()
        """
        raise RuntimeError("%s#on_enter() is not implemented" % self.__class__.__name__)
