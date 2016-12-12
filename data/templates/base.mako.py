# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317664232.309885
_template_filename=u'/home/cctsg/software/DARE-NGS/darengs/templates/base.mako'
_template_uri=u'/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> \n<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="en-US"> \n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> \n \n<title>DARE-NGS</title> \n  ')
        # SOURCE LINE 6
        __M_writer(escape(h.stylesheet_link(url('/style.css'))))
        __M_writer(u'\n\n<link rel="stylesheet" href="')
        # SOURCE LINE 8
        __M_writer(escape(url('/newtheme/js/prettyPhoto/css/prettyPhoto.css')))
        __M_writer(u'" type="text/css" media="screen"/> \n<link rel="stylesheet" href="')
        # SOURCE LINE 9
        __M_writer(escape(url('/newtheme/style.css')))
        __M_writer(u'" type="text/css" media="screen" /> \n<link rel="stylesheet" type="text/css" media="all" href="')
        # SOURCE LINE 10
        __M_writer(escape(url('/newtheme/styles/minimal_soft_green.css')))
        __M_writer(u'" /> \n \n<script type="text/javascript"> \n/* <![CDATA[ */\ndocument.write(\'<style type="text/css">h1,h2,h3,h4,h5,#blurb,#site_name,#intro_blurb_title,#call_to_action,.light_gradient.dropcap1,.widgettitle,.dropcap2,.dark_gradient,th{text-indent:-9999px;}.noscript{display:none;}.bg_hover{background:none;}</style>\');\n/* ]]> */\n</script> \n\n<script type="text/javascript" language="javascript">\n<!-- //\nfunction checkform(){\n    var elLength = document.chipseq.elements.length;\n    var message = " ";\n    for (i=0; i<elLength; i++)\n    {\n       var name = document.chipseq.elements[i].name;\n       var type = document.chipseq.elements[i].type;\n       \n       if (type=="text"){\n            message = message + "\\n"+ name + " = " ;\n            var value = document.chipseq.elements[i].value;\n            message = message +" : " +value;\n        }\n       if (type=="select-one"){\n            message = message + "\\n"+ name + " = " ;\n            var value = document.chipseq.elements[i].value;\n            message = message+value;\n        }              \n    }\n    \n    var answer = confirm (message + " \\n Are these ok?")\n    if (answer)\n         return true;\n    else\n         return false;\n\n}\n// -->\n</script>\n\n\n<meta name="disable_cufon" content="" />\n<meta name="slider_speed" content="7000" />\n<meta name="slider_disable" content="false" />\n<meta name="slider_type" content="fading" />\n \n<script type=\'text/javascript\' SRC="')
        # SOURCE LINE 56
        __M_writer(escape(url('/newtheme/js/swfobject.js')))
        __M_writer(u'"></script> \n<script type=\'text/javascript\' SRC="')
        # SOURCE LINE 57
        __M_writer(escape(url('/newtheme/js/jquery/jquery.js')))
        __M_writer(u'"></script> \n<script type=\'text/javascript\' SRC="')
        # SOURCE LINE 58
        __M_writer(escape(url('/newtheme/js/jquery.easing.js')))
        __M_writer(u'"></script> \n<script type=\'text/javascript\' SRC="')
        # SOURCE LINE 59
        __M_writer(escape(url('/newtheme/js/cufon-yui.js')))
        __M_writer(u'"></script> \n<script type=\'text/javascript\' SRC="')
        # SOURCE LINE 60
        __M_writer(escape(url('/newtheme/js/DejaVu_Sans_Condensed_400.font.js')))
        __M_writer(u'"></script> \n<script type=\'text/javascript\' SRC="')
        # SOURCE LINE 61
        __M_writer(escape(url('/newtheme/js/prettyPhoto/js/jquery.prettyPhoto.js')))
        __M_writer(u'"></script> \n<script type=\'text/javascript\' SRC="')
        # SOURCE LINE 62
        __M_writer(escape(url('/newtheme/js/jquery.tools.min.js')))
        __M_writer(u'"></script> \n<script type=\'text/javascript\' SRC="')
        # SOURCE LINE 63
        __M_writer(escape(url('/newtheme/js/galleria/galleria.js')))
        __M_writer(u'"></script> \n<script type=\'text/javascript\' SRC="')
        # SOURCE LINE 64
        __M_writer(escape(url('/newtheme/js/galleria/themes/classic/galleria.classic.js')))
        __M_writer(u'"></script> \n<script type=\'text/javascript\' SRC="')
        # SOURCE LINE 65
        __M_writer(escape(url('/newtheme/js/custom.js')))
        __M_writer(u'"></script> \n<script type=\'text/javascript\' SRC="')
        # SOURCE LINE 66
        __M_writer(escape(url('/newtheme/js/sliders.js')))
        __M_writer(u'"></script> \n\n<script type="text/javascript"> \n/* <![CDATA[ */\n\tvar vvqflashvars = {};\n\tvar vvqparams = { wmode: "opaque", allowfullscreen: "true", allowscriptacess: "always" };\n\tvar vvqattributes = {};\n\tvar vvqexpressinstall = "')
        # SOURCE LINE 73
        __M_writer(escape(url('/newtheme/js/expressinstall.swf')))
        __M_writer(u'";\n/* ]]> */\n</script> \n \n<!--[if IE 8]>\n\t<link rel="stylesheet" href="styles/_shared/ie8.css" type="text/css" media="screen" />\n<![endif]--> \n \n<!--[if IE 7]>\n\t<link rel="stylesheet" href="styles/_shared/ie7.css" type="text/css" media="screen" />\n<![endif]--> \n\n</head> \n \n<body onload="doLoad()" > \n \n<div class="body_background"> \n\t<div id="header"> \n\t\t<div class="inner"> \n\t\t\n\t\t\t<!-- logo -->\n\t\t\t<div id="logo"> \n\t\t\t\t<a HREF="')
        # SOURCE LINE 95
        __M_writer(escape(url('/')))
        __M_writer(u'"><img SRC="')
        __M_writer(escape(url('/newtheme/styles/minimal_soft_green/DARE.png')))
        __M_writer(u'" alt="" width="178" height="72" /></a>\n\t\t\t</div> \n\t\t\t\n\t\t\t<!-- LOGIN -->\n\t\t\t<div id="social_header" style="top:121px;">\n')
        # SOURCE LINE 100
        if c.userid=="false":
            # SOURCE LINE 101
            __M_writer(u'     <a href="')
            __M_writer(escape(url('/users/login')))
            __M_writer(u'">Login</a><br/>\n     <a href="')
            # SOURCE LINE 102
            __M_writer(escape(url('/users/register')))
            __M_writer(u'">Register</a>\n')
            # SOURCE LINE 103
        else:
            # SOURCE LINE 104
            __M_writer(u'\t<a href="')
            __M_writer(escape(url('/users/logout')))
            __M_writer(u'">Logout</a><br/>\n')
            pass
        # SOURCE LINE 106
        __M_writer(u'\t\t\t</div>\t\t\n\t\t\t\n\t\t\t<!-- navigation -->\n\t\t\t<div id="main_navigation" class="jqueryslidemenu unitPng">\n\t\t\t\t<ul>\n\t\t\t\t\t  <li><a href="')
        # SOURCE LINE 111
        __M_writer(escape(url('/')))
        __M_writer(u'">HOME</a></li>\n      <li><a href="')
        # SOURCE LINE 112
        __M_writer(escape(url('/ngs/about')))
        __M_writer(u'">ABOUT DARE-NGS</a>\n         <ul>\n\n            <li ><a title="Pipeline"  href="')
        # SOURCE LINE 115
        __M_writer(escape(url('/ngs/resources')))
        __M_writer(u'" >Resources</a></li>\n            <li ><a title="Pipeline"  href="')
        # SOURCE LINE 116
        __M_writer(escape(url('/ngs/trac')))
        __M_writer(u'" >Trac DARE</a></li>\n            <li ><a title="Pipeline"  href="')
        # SOURCE LINE 117
        __M_writer(escape(url('/ngs/using_bfast')))
        __M_writer(u'" >Using Bfast</a></li>\n            <li ><a title="Pipeline"  href="')
        # SOURCE LINE 118
        __M_writer(escape(url('/ngs/using_chipseq')))
        __M_writer(u'" >Using CHiP-SEQ</a></li>\n            <li ><a title="Pipeline"  href="')
        # SOURCE LINE 119
        __M_writer(escape(url('/ngs/using_tophatfusion')))
        __M_writer(u'" >Using TophatFusion</a></li>\n\n        </ul>\n \n      </li>\n\n      <li><a class="MenuBarItemSubmenu"> JOB SUBMISSION </a>\n        <ul>\n\n          <li ><a title="Pipeline"  href="')
        # SOURCE LINE 128
        __M_writer(escape(url('/ngs/bfast_form')))
        __M_writer(u'" >BFAST</a></li>\n          <li ><a title="Pipeline"  href="')
        # SOURCE LINE 129
        __M_writer(escape(url('/ngs/chipseq_form')))
        __M_writer(u'" >ChIP-SEQ</a></li>\n          <li ><a title="Pipeline"  href="')
        # SOURCE LINE 130
        __M_writer(escape(url('/ngs/tophatfusion_form')))
        __M_writer(u'" >TOPHAT-FUSION</a></li>\n')
        # SOURCE LINE 131
        if c.userid!="false":      
            pass
        # SOURCE LINE 133
        __M_writer(u'          <li><a href="')
        __M_writer(escape(url('/ngs/dalliance')))
        __M_writer(u'">Dalliance</a></li>\n          <li><a href="')
        # SOURCE LINE 134
        __M_writer(escape(url('/ngs/job_table_view')))
        __M_writer(u'">Job Table View</a></li>\n          \n        </ul>\n      </li>\n      <li><a href="')
        # SOURCE LINE 138
        __M_writer(escape(url('/ngs/software')))
        __M_writer(u'">SOFTWARE</a></li>\n      <li><a href="')
        # SOURCE LINE 139
        __M_writer(escape(url('/ngs/contact')))
        __M_writer(u'">CONTACT</a></li>\n\t\t\t\t</ul>\n\t\t\t</div> \n\t\t</div><!-- inner --> \n\t</div><!-- header --> \n\n\t<div id="body_block" class="full_width fading framed minimal_soft_green"> \n\t\n\t\t\t\n\t\t<div id="intro_blurb">\n\t\t')
        # SOURCE LINE 149
        flash_message = h.flash.pop_message()  
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['flash_message'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        # SOURCE LINE 150
        if flash_message: 
            # SOURCE LINE 151
            __M_writer(u'     <div id="flash-message">')
            __M_writer(filters.html_escape(escape(flash_message )))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 153
        __M_writer(u'\n\t\t\t<div class="inner">\t\n \t\t\t<!--\t<a class="button_link alignright large_button" href=""><span>Learn More</span></a> -->\t\n \t\t\t\t')
        # SOURCE LINE 156
        __M_writer(escape(self.body()))
        __M_writer(u'\n\n    </div><!-- inner --> \n\t\t</div><!-- intro_blurb --> \n\t\t\t\t\t\t\t\t\n\t</div><!-- body_block --> \n \n\t<div id="footer"> \n\n\t</div><!-- footer --> \n \n</div><!-- body_background --> \n\n</body> \n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


