import logging

from plone import api
from plone.base.interfaces.installable import INonInstallable
from Products.CMFCore.WorkflowTool import WorkflowTool
from Products.GenericSetup.tool import SetupTool
from zope.interface import implementer

logger = logging.getLogger(__name__)


@implementer(INonInstallable)
class HiddenProfiles:
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "v2tec.intranet:uninstall",
        ]

    def getNonInstallableProducts(self):
        """Hide the upgrades package from site-creation and quickinstaller."""
        return [
            "v2tec.intranet.upgrades",
        ]


def fecha_intranet(portal_setup: SetupTool):
    """Aplica novo workflow para a intranet."""
    wf_tool: WorkflowTool = api.portal.get_tool("portal_workflow")
    wf_tool.updateRoleMappings()
    logger.info("Permissões de workflow atualizadas")
