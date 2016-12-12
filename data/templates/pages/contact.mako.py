# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317665613.4451931
_template_filename='/home/cctsg/software/DARE-NGS/darengs/templates/pages/contact.mako'
_template_uri='/pages/contact.mako'
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
        __M_writer(u'\n\n<p> \nThis project is being developed by Cyber-Infrastructure Develop (CyD) Group at Center for Computational Technology(CCT)</p>\n \n <p><b>Project Lead:</b><br />\n      Dr. Shantenu Jha <br />\n      Email: <a href="mailto:sjha@cct.lsu.edu"> sjha@cct.lsu.edu</a>\n</p>\n      \n    <p><b>Gateway Development Lead:</b><br />\n       Dr. Joohyun Kim<br/>\n       Email: <a href="mailto:jhkim@cct.lsu.edu"> jhkim@cct.lsu.edu</a>\n</p>\n\n  <p><b>Developer:</b><br />\n       Sharath Maddineni<br/>\n       Email: <a href="mailto:smaddineni@cct.lsu.edu"> smaddineni@cct.lsu.edu</a>\n</p>\n<p>\n<b>\nFunding:\n</b><br />\nNIH-LBRN, internal resources at CCT, LSU and NSF for support of SAGA\n</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


