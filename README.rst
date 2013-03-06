.. contents::

Introduction
============

This add-one shows a badge with custom text in right upper corner of the page.


Installation
============
    
You can install this add-one using either ``setup.py`` file or ``buildout.cfg`` 
file.

Installation using setup.py file
--------------------------------

To install this add-one using setup.py you have to launch command prompt, change
to the directory with setup.py file and type

``python setup.py install``

to install in production mode

or

``python setup.py develop``

to install in development mode.


Installation using buildout.cfg file
------------------------------------

To install this add-on using buildout.cfg file you need to do next things:

   1. Add the following to your buildout.cfg file.
      
      
      ``[buildout]``
      
      ``...``
      
      ``eggs = collective.demositebadge``
      
      
      
   2. Rerun buildout and restart your Zope instance.
   3. Install the Add-on in Your Plone Site. Go to ``Site Setup -> Add-ons``, 
      find ``collective.demositebadge``, check it and press ``Activate`` button.
      After doing that you should see this:
      
.. image:: ./badge.png

   4. After that go to ``Zope management interface ->portal-javascripts``, 
      find ``demo-site-badge.js`` and check ``Inline rendering`` checkbox 

Installation on Plone 3
------------------------
To install this package on Plone 3 you need to do step 1 from 
``Installation using buildout.cfg file``, and also do next things:

       1. Add the following to your buildout.cfg file:
       
       ``[buildout]``
       
       ``...`` 
       
       ``extends = ``
             ``http://good-py.appspot.com/release/plone.app.registry/1.0b1``
       
       ``...``
      
      ``[versions]``
      
      ``plone.z3cform = 0.6.0``
      ``zope.i18n = 3.6.0``
      
      ``[instance]``
      
      ``...``
      
        ``zcml = ``
              ``plone.app.registry``          
       
       2. After rerunning buildout.cfg and restarting Zope instance go to 
          ``Site Setup -> Add-ons`` find ``Configuration registry 1.0b1 ``
          and activate it.
       
       3. Do step 4 from ``Installation using buildout.cfg file``.

Usage
=====

Go to ``Site Setup-> Add-on Configuration`` and follow the ``Demo site badge``
link.
Type some text into ``Text to show`` field, check ``Display badge`` checkbox
and press the ``Save`` button. 


Notes
=====
If you are using Firefox 4 browser you can face a problem that DemoSite Badge 
doesn't react on the switches. To solve this problem you should disable
``base2-dom-fp.js`` on ``portal_javascripts``
