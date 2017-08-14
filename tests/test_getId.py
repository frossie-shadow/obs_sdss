#!/usr/bin/env python

#
# LSST Data Management System
# Copyright 2008-2015 AURA/LSST.
#
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <https://www.lsstcorp.org/LegalNotices/>.
#

import unittest
import lsst.utils.tests

import lsst.daf.persistence as dafPersist
from lsst.obs.sdss import SdssMapper


class GetIdTestCase(lsst.utils.tests.TestCase):
    """Testing butler exposure id retrieval"""

    def setUp(self):
        self.bf = dafPersist.ButlerFactory(mapper=SdssMapper(root="."))
        self.butler = self.bf.create()

    def tearDown(self):
        del self.butler
        del self.bf

    def testId(self):
        """Test retrieval of exposure ids"""
        bits = self.butler.get("ccdExposureId_bits")
        self.assertEqual(bits, 38)
        id = self.butler.get("ccdExposureId", run=6537,
                             camcol=3, filter='r', field=514)
        self.assertEqual(id, 6537230514)
        id = self.butler.get("ccdExposureId", run=4933,
                             camcol=3, filter='g', field=748)
        self.assertEqual(id, 4933130748)

        dataId = dict(tract=1, patch='2,3', filter='z')
        bits = self.butler.get("deepCoaddId_bits", dataId)
        id = self.butler.get("deepCoaddId", dataId)
        self.assertEqual(bits, 37)
        self.assertEqual(id, ((((1 * 8192) + 2) * 8192) + 3)*8 + 4)


class TestMemory(lsst.utils.tests.MemoryTestCase):
    pass


def setup_module(module):
    lsst.utils.tests.init()

if __name__ == "__main__":
    lsst.utils.tests.init()
    unittest.main()
