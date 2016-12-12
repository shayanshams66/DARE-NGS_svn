# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317664253.3215301
_template_filename='/home/cctsg/software/DARE-NGS/darengs/templates/forms/chipseq_form.mako'
_template_uri='/forms/chipseq_form.mako'
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
        __M_writer(u'\n\n\n<div style="width: 60%; float:left">\n\n')
        # SOURCE LINE 8
        __M_writer(u'\n\n<H2> ChIP-SEQ </H2>\nFigure on the right shows the Pipeline and Tools used\n\n<p>  Choose the reference genome and the location of your sequenced data </p>\n<p> (Note that this service is only available for a user who has an account with LONI machines) </p>\n<form name="chipseq" method="POST" enctype="multipart/form-data" action="')
        # SOURCE LINE 15
        __M_writer(escape(url('/ngs/job_insert')))
        __M_writer(u'">\n\n<table border="0"  cellspacing="0" cellpadding="5">\n')
        # SOURCE LINE 18
        for field in c.form:
            # SOURCE LINE 19
            if field.is_hidden:
                # SOURCE LINE 20
                __M_writer(u'     ')
                __M_writer(escape(field))
                __M_writer(u' \n')
                # SOURCE LINE 21
            else:      
                # SOURCE LINE 22
                __M_writer(u'\n\t   <tr>\t\n\t\t<td> ')
                # SOURCE LINE 24
                __M_writer(escape( field.label_tag() ))
                __M_writer(u'   </td>\n\t\t<td> ')
                # SOURCE LINE 25
                __M_writer(escape( field ))
                __M_writer(u' </td>\n\t\t<td> ')
                # SOURCE LINE 26
                __M_writer(escape( field.errors ))
                __M_writer(u' </td>\n\t   </tr>\n')
                pass
            pass
        # SOURCE LINE 30
        __M_writer(u'</table>  \n\n<input type="submit" name="Submit" value="Submit" onclick="return checkform()" />\n\n\n</form>\n</div>\n\n<div style="width: 40%; float:right">\n        <img src="')
        # SOURCE LINE 39
        __M_writer(escape(url('/workflow_Chipseq.png')))
        __M_writer(u'"  />\n</div>\n')
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


