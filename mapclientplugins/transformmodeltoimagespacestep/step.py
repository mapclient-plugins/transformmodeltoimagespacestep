import json

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.transformmodeltoimagespacestep.configuredialog import ConfigureDialog

from gias3.image_analysis import fw_segmentation_tools as fst


class TransformModeltoImageSpaceStep(WorkflowStepMountPoint):

    def __init__(self, location):
        super(TransformModeltoImageSpaceStep, self).__init__('Transform Model to Image Space', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Registration'
        # Add any other initialisation code here:
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#fieldworkmodeldict'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#giasscandict'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#fieldworkmodeldict'))
        self._config = {'identifier': '', 'Mirror': 'False', 'Z Shift': 'False'}

        self._scan = None
        self._inputModelDict = None
        self._outputModelDict = None

    def execute(self):
        if self._config['Mirror'] == 'False':
            ns = False
        elif self._config['Mirror'] == 'True':
            ns = True

        if self._config['Z Shift'] == 'False':
            zs = False
        elif self._config['Z Shift'] == 'True':
            zs = True

        self._outputModelDict = {}
        for name, gf in list(self._inputModelDict.items()):
            self._outputModelDict[name] = fst.makeImageSpaceGF(self._scan, gf, negSpacing=ns, zShift=zs)

        self._doneExecution()

    def setPortData(self, index, dataIn):
        if index == 1:
            if len(dataIn) > 1:
                raise ValueError('only one image supported.')

            self._scan = list(dataIn.values())[0]  # ju#giasscandict
        else:
            self._inputModelDict = dataIn  # ju#fieldworkmodeldict

    def getPortData(self, index):
        return self._outputModelDict

    def configure(self):
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        return self._config['identifier']

    def setIdentifier(self, identifier):
        self._config['identifier'] = identifier

    def serialize(self):
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()
