from lsst.obs.sdss.calibrate import SdssCalibrateTask
root.calibrate.retarget(SdssCalibrateTask)

import lsst.meas.astrom.catalogStarSelector
root.calibrate.u.starSelector.name = "catalog"
root.calibrate.z.starSelector.name = "catalog"
root.detection.background.binSize = 512

import lsst.meas.extensions.multiShapelet
root.measurement.algorithms.names += ("multishapelet.psf", "multishapelet.exp", "multishapelet.dev", 
                                      "multishapelet.combo")
root.measurement.apCorrFluxes += ("multishapelet.exp.flux", "multishapelet.dev.flux",
                                  "multishapelet.combo.flux")
root.measurement.slots.modelFlux = "multishapelet.combo.flux"
