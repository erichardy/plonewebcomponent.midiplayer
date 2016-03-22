# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonewebcomponent.midiplayer


class PlonewebcomponentMidiplayerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=plonewebcomponent.midiplayer)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonewebcomponent.midiplayer:default')


PLONEWEBCOMPONENT_MIDIPLAYER_FIXTURE = PlonewebcomponentMidiplayerLayer()


PLONEWEBCOMPONENT_MIDIPLAYER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONEWEBCOMPONENT_MIDIPLAYER_FIXTURE,),
    name='PlonewebcomponentMidiplayerLayer:IntegrationTesting'
)


PLONEWEBCOMPONENT_MIDIPLAYER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONEWEBCOMPONENT_MIDIPLAYER_FIXTURE,),
    name='PlonewebcomponentMidiplayerLayer:FunctionalTesting'
)


PLONEWEBCOMPONENT_MIDIPLAYER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONEWEBCOMPONENT_MIDIPLAYER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonewebcomponentMidiplayerLayer:AcceptanceTesting'
)
