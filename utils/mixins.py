""" Utils mixins. """

class PageTitleMixin(object):
  """ Set page_title attribute in context. """
  def get_page_title(self, context):
    return getattr(self, 'page_title', 'HEALTH')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_title'] = self.get_page_title(context)

    return context