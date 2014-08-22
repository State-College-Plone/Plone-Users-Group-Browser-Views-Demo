from Products.Five.browser import BrowserView


class TestView(BrowserView):

    def total(self):
        number1 = self.request.get('number1', 0)
        number2 = self.request.get('number2', 0)
        return number1 + number2


class OtherTestView(BrowserView):

    def __call__(self):
        import pdb; pdb.set_trace( )
        return "It's not the site root!"


class ThumbnailView(BrowserView):

    def __call__(self):
        return "Success!"


class Related(BrowserView):

    def __call__(self):
        related = self.context.getRelatedItems()
        if related:
            return related[0].absolute_url()
