# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1314721427.256242
_template_filename='/home/cctsg/software/DARE-NGS/darengs/templates/users/register.mako'
_template_uri='/users/register.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from markupsafe import escape
_exports = ['pagetitle']


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
        url = context.get('url', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\t<br/>\n\t<br/>\n')
        # SOURCE LINE 4
        __M_writer(escape(c.display_message))
        __M_writer(u'\n\n')
        # SOURCE LINE 8
        __M_writer(u'\n<form name="user_login" method="POST" action="')
        # SOURCE LINE 9
        __M_writer(escape(url('/users/register_post')))
        __M_writer(u'">\n\n<table border="0"  cellspacing="0" cellpadding="5">\n')
        # SOURCE LINE 12
        for field in c.form:
            # SOURCE LINE 13
            __M_writer(u'\t   <tr>\t\t\n\t\t<td> ')
            # SOURCE LINE 14
            __M_writer(escape( field.label_tag() ))
            __M_writer(u'   </td>\n\t\t<td> ')
            # SOURCE LINE 15
            __M_writer(escape( field ))
            __M_writer(u' </td>\n\t\t<td> ')
            # SOURCE LINE 16
            __M_writer(escape( field.errors ))
            __M_writer(u' </td>\n\t   </tr>  \n')
            pass
        # SOURCE LINE 19
        __M_writer(u'</table>  \n\n<input type="submit" name="submit" value="Submit" />\n\n</form>\n')
        # SOURCE LINE 24
        if c.email == "invalid":
            # SOURCE LINE 25
            __M_writer(u' <p>Given email already exists. Please use a different email</p>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagetitle(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\nJob Submission\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


