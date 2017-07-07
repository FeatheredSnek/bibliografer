# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

import Bibliografer

def index():
	session.entries_list = [('book', {'year': '1994', 'publisher': 'Cornell University Press', 'authors': 'Lloyd Genevieve', 'title': 'Part of Nature: Self-Knowledge in Spinoza&#39;s Ethics'}), ('article', {'pages': '342-359', 'year': '2013', 'journal': 'Deleuze Studies', 'title': 'Nomadic Ethics', 'authors': 'Braidotti Rosi', 'issue': '7 (3)'}), ('chapter', {'authors': 'Smart J. J. C.', 'booktitle': 'Contemporary Debates in Metaphysics' , 'publisher': 'Blackwell', 'title': 'The tenseless theory of time', 'year': '2008', 'pages': '226-38', 'editors': 'Theodore Sider, John Hawthorne &amp; Dean W. Zimmerman (eds.)'})]
	return dict()

def gotowe():
	session.docx_filename = str(hash(str(session.entries_list)))
	session.testvar = Bibliografer.testloop(session.entries_list, session.docx_filename)
	session.docx_url = session.docx_filename + '.docx'
	return dict(view_list=session.testvar, view_url=session.docx_url)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
