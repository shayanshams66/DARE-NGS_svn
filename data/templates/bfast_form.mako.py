# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1314726490.844913
_template_filename='/home/cctsg/software/DARE-NGS/darengs/templates/bfast_form.mako'
_template_uri='/bfast_form.mako'
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
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n<div style="width: 60%; float:left">\n\t<br/>\n\t<br/>\n\n')
        # SOURCE LINE 9
        __M_writer(u'\n\n<H2> Genome-wide Mapping with BFAST </H2>\nFigure on the right shows the Pipeline and Tools Used\n<p>  Choose the reference genome and the location of your sequenced data </p>\n<p> (Note that this service is only available for a user who has an account with LONI machines) </p>\n<form name="bfast_input" method="POST" enctype="multipart/form-data" action="')
        # SOURCE LINE 15
        __M_writer(escape(url('/ngs/job_insert')))
        __M_writer(u'">\n\n<table border="0"  cellspacing="0" cellpadding="5">\n\n')
        # SOURCE LINE 19
        for field in c.form:   
            # SOURCE LINE 20
            __M_writer(u'\n')
            # SOURCE LINE 21
            if field.is_hidden:
                # SOURCE LINE 22
                __M_writer(u'     ')
                __M_writer(escape(field))
                __M_writer(u' \n')
                # SOURCE LINE 23
            else:      
                # SOURCE LINE 24
                __M_writer(u'\n\t   <tr>\t\n\t\t<td > ')
                # SOURCE LINE 26
                __M_writer(escape( field.label_tag() ))
                __M_writer(u'   </td>\n\t\t<td > ')
                # SOURCE LINE 27
                __M_writer(escape( field ))
                __M_writer(u' </td>\n\t\t<td> ')
                # SOURCE LINE 28
                __M_writer(escape( field.errors ))
                __M_writer(u' </td>\n\t   </tr>\n')
                pass
            # SOURCE LINE 31
            __M_writer(u'\n')
            pass
        # SOURCE LINE 33
        __M_writer(u'</table>  \n<input type="submit" name="Submit" value="Submit" />\n</form>\n</div>\n\n<div style="width: 40%; float:right">\n        <img src="')
        # SOURCE LINE 39
        __M_writer(escape(url('/workflow_BFAST.png')))
        __M_writer(u'"  />\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagetitle(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\nJob Submission\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


