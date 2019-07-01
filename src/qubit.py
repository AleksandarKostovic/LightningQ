"""
MIT License

Copyright (c) 2019 Aleksandar Kostovic

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Qubit

import nazca as nd
import nazca.demofab as demo

# Mach-Zehnder Interferometer- MZI
with nd.Cell("MZI") as mzi:
    # Upper arm
    demo.shallow.strt(length=10).put(0)
    demo.shallow.sinebend(distance=100, offset=40).put()
    demo.s2d().put()
    ps = demo.eopm_dc(length=150).put()
    demo.d2s().put()
    demo.shallow.sinebend(distance=100, offset=-40).put()
    demo.shallow.strt(length=10).put()
    # Pads
    pad1 = demo.pad_dc().put(ps.pin["c0"].move(300, 200, 0))
    demo.metaldc.sbend_p2p(ps.pin["c0"], Lstart=200).put()
    pad2 = demo.pad_dc().put(ps.pin["c1"].move(300, 100, 0))
    demo.metaldc.sbend_p2p(ps.pin["c1"], Lstart=200).put()
    # Lower arm
    demo.shallow.strt(length=10).put(0, -20)
    demo.shallow.sinebend(distance=100, offset=-40).put()
    demo.shallow.strt(length=300).put()
    demo.shallow.sinebend(distance=100, offset=40).put()
    demo.shallow.strt(length=10).put()
    #Pins
    nd.Pin('c0', pin=demo.eopm_dc().pin['c0']).put()
    nd.Pin('c1', pin=demo.eopm_dc().pin['c1']).put()
    nd.Pin('c2', pin=demo.eopm_dc().pin['c0']).put()
    nd.Pin('c3', pin=demo.eopm_dc().pin['c1']).put()
    
# Directional Coupler
with nd.Cell("Direction Coupler") as dc:
    # Upper Arm
    demo.shallow.sinebend(distance=100, offset=240).put(0)
    demo.shallow.strt(length=20).put()
    demo.shallow.sinebend(distance=100, offset=-220).put()
    demo.shallow.strt(length=10).put()
    # Lower Arm
    demo.shallow.sinebend(distance=100, offset=-240).put(0, -20)
    demo.shallow.strt(length=20).put()
    demo.shallow.sinebend(distance=100, offset=220).put()
    demo.shallow.strt(length=10).put()

# De-Coupler
with nd.Cell("De-Coupler") as dec:
    # Upper Arm
    demo.shallow.sinebend(distance=100, offset=-40).put(0, 40)
    demo.shallow.strt(length=10).put()
    # Lower Arm
    demo.shallow.sinebend(distance=100, offset=40).put(0, -60)
    demo.shallow.strt(length=10).put()

# Qubit constructed from three MZIs
with nd.Cell("Qubit") as qubit:
    dec.put(0)
    mzi.put(110)
    mzi.put(630)
    mzi.put(1150)
    dc.put(1670)

 
# First Qubit
qubit.put(0)

# Second Qubit
qubit.put(0, -520)

# Third Qubit
qubit.put(0, -1040)

# Fourth Qubit
qubit.put(0, -1560)

# Export a GDS file
nd.export_gds()
