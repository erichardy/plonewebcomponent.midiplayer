# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plonewebcomponent.midiplayer.testing import PLONEWEBCOMPONENT_MIDIPLAYER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonewebcomponent.midiplayer is properly installed."""

    layer = PLONEWEBCOMPONENT_MIDIPLAYER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonewebcomponent.midiplayer is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonewebcomponent.midiplayer'))

    def test_browserlayer(self):
        """Test that IPlonewebcomponentMidiplayerLayer is registered."""
        from plonewebcomponent.midiplayer.interfaces import (
            IPlonewebcomponentMidiplayerLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonewebcomponentMidiplayerLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONEWEBCOMPONENT_MIDIPLAYER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonewebcomponent.midiplayer'])

    def test_product_uninstalled(self):
        """Test if plonewebcomponent.midiplayer is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonewebcomponent.midiplayer'))

    def test_browserlayer_removed(self):
        """Test that IPlonewebcomponentMidiplayerLayer is removed."""
        from plonewebcomponent.midiplayer.interfaces import IPlonewebcomponentMidiplayerLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonewebcomponentMidiplayerLayer, utils.registered_layers())
