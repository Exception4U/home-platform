# Copyright (c) 2017, IGLU consortium
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
#  - Redistributions of source code must retain the above copyright notice, 
#    this list of conditions and the following disclaimer.
#  - Redistributions in binary form must reproduce the above copyright notice, 
#    this list of conditions and the following disclaimer in the documentation 
#    and/or other materials provided with the distribution.
#  - Neither the name of the copyright holder nor the names of its contributors 
#    may be used to endorse or promote products derived from this software 
#    without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT 
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, 
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
# POSSIBILITY OF SUCH DAMAGE.

import os
import time
import logging
import numpy as np
import unittest

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data")
TEST_SUNCG_DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "suncg")

from panda3d.core import LMatrix4f, LMatrix4, LVector3

from multimodalmaze.suncg import SunCgSceneLoader
from multimodalmaze.utils import Viewer, mat4ToNumpyArray, vec3ToNumpyArray
    
class TestViewer(unittest.TestCase):
    
    def testStep(self):
        
        try:
            scene = SunCgSceneLoader.loadHouseFromJson("0004d52d1aeeb8ae6de39d6bd993e992", TEST_SUNCG_DATA_DIR)

            #NOTE: show initial models loaded into the scene
            for model in scene.scene.findAllMatches('**/+ModelNode'):
                model.show()
    
            viewer = Viewer(scene, shadowing=False)
            
            # Configure the camera
            #NOTE: in Panda3D, the X axis points to the right, the Y axis is forward, and Z is up
            mat = np.array([0.999992, 0.00394238, 0, 0,
                            -0.00295702, 0.750104, -0.661314, 0,
                            -0.00260737, 0.661308, 0.75011, 0,
                            43.621, -55.7499, 12.9722, 1])
            mat = LMatrix4f(*mat.ravel())
            viewer.cam.setMat(mat)
            
            for _ in range(20):
                viewer.step()
            time.sleep(1.0)
        
        finally:
            viewer.destroy()
            viewer.graphicsEngine.removeAllWindows()

class TestFunctions(unittest.TestCase):
    
    def testMat4ToNumpyArray(self):
        xr = np.random.random((4,4))
        mat = LMatrix4(*xr.ravel())
        x = mat4ToNumpyArray(mat)
        self.assertTrue(np.allclose(x, xr, atol=1e-6))
        
    def testVec3ToNumpyArray(self):
        xr = np.random.random((3,))
        vec = LVector3(*xr.ravel())
        x = vec3ToNumpyArray(vec)
        self.assertTrue(np.allclose(x, xr, atol=1e-6))
        
if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    np.seterr(all='raise')
    unittest.main()
    