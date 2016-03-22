.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

============================
plonewebcomponent.midiplayer
============================

Tell me what your product does

Features
--------

- Can be bullet points


Examples
--------

This add-on can be seen in action at the following sites:
- Is there a page on the internet where everybody can see the features?


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install plonewebcomponent.midiplayer by adding it to your buildout::

    [buildout]

    ...

    eggs =
        plonewebcomponent.midiplayer


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/plonewebcomponent.midiplayer/issues
- Source Code: https://github.com/collective/plonewebcomponent.midiplayer
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.




<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"
      xmlns:tal="http://xml.zope.org/namespaces/tal"
      xmlns:metal="http://xml.zope.org/namespaces/metal"
      xmlns:i18n="http://xml.zope.org/namespaces/i18n"
      lang="en"
      metal:use-macro="context/main_template/macros/master"
      i18n:domain="plone">

<body>

    <metal:content-core fill-slot="content-core">
<link rel="import" href="++resource++midiplayer/midi-player.html">

<midi-player url="++resource++midiplayer/ColmanCross1.mid"></midi-player>

    </metal:content-core>

</body>
</html>


