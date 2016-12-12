# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1316150966.310091
_template_filename='/home/cctsg/software/DARE-NGS/darengs/templates/pages/trac.mako'
_template_uri='/pages/trac.mako'
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
        __M_writer(u'\nPlease visit the trac for DARE to open a ticket\n<br/>\n<a href="http://cyder.cct.lsu.edu:8080/trac-dare/" > Click Here </a>\n<br/>\n\nlogin using  \n<br/>\nusername: guest\n<br/>\npassword: guest\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


