# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1316150970.398484
_template_filename='/home/cctsg/software/DARE-NGS/darengs/templates/pages/using_tophatfusion.mako'
_template_uri='/pages/using_tophatfusion.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from markupsafe import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n    <H2 align="justify"><br />\n      <font color=\'#00007A\'> DARE-NGS </font> <br />\n     </H2>\n\n<ul>\n<li><H4>How TopHatFusion is carried out?</H4>\n<p>\n\n</p>\n</li>\n<li><H4>Input DATA?</H4>\n<p>\nWill be provided by the user prior to submitting a job\n</p>\n\n</li>\n<li><H4>Features</H4>\n<p>\nDistributed Computing\n</p>\n\n</li>\n<li><H4>Advantages</H4>\n<p>\nUsability and Scalability along with faster results due to Distributed  Computing\n</p>\n</li>\n\n</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


