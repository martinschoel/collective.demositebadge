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

      


Usage
=====

Go to ``Site Setup-> Add-on Configuration`` and follow the ``Demo site badge``
link.
Type some text into ``Text to show`` field, check ``Display badge`` checkbox
and press the ``Save`` button. 
