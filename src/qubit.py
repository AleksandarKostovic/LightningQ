# Qubit

import nazca as nd
import nazca.demofab as demo

with nd.Cell("Qubit") as qubit:
    # Upper arm
    demo.shallow.sinebend(distance=100, offset=-40).put(0, 50)
    demo.shallow.strt(length=20).put()
    demo.shallow.sinebend(distance=100, offset=40).put()
    demo.s2d().put()
    ps = demo.eopm_dc(length=150).put()
    demo.d2s().put()
    demo.shallow.sinebend(distance=100, offset=-40).put()
    demo.shallow.strt(length=20).put()
    demo.shallow.sinebend(distance=100, offset=40).put()
    # Pads
    pad1 = demo.pad_dc().put(ps.pin["c0"].move(300, 200, 0))
    demo.metaldc.sbend_p2p(ps.pin["c0"], Lstart=200).put()
    pad2 = demo.pad_dc().put(ps.pin["c1"].move(300, 100, 0))
    demo.metaldc.sbend_p2p(ps.pin["c1"], Lstart=200).put()
    # Lower arm
    demo.shallow.sinebend(distance=100, offset=40).put(0, -50)
    demo.shallow.strt(length=20).put()
    demo.shallow.sinebend(distance=100, offset=-40).put()
    demo.shallow.strt(length=300).put()
    demo.shallow.sinebend(distance=100, offset=40).put()
    demo.shallow.strt(length=20).put()
    demo.shallow.sinebend(distance=100, offset=-40).put()
    #Pinzz
    nd.Pin('c0', pin=demo.eopm_dc().pin['c0']).put()
    nd.Pin('c1', pin=demo.eopm_dc().pin['c1']).put()
    nd.Pin('c2', pin=demo.eopm_dc().pin['c0']).put()
    nd.Pin('c3', pin=demo.eopm_dc().pin['c1']).put()

with nd.Cell("Qubit2") as qubit2:
    demo.shallow.sinebend(distance=100, offset=-40).put(0, 50)
    demo.shallow.strt(length=20).put()
    demo.shallow.sinebend(distance=100, offset=40).put()
    demo.s2d().put()
    ps = demo.eopm_dc(length=150).put()
    demo.d2s().put()
    demo.shallow.sinebend(distance=100, offset=200).put()
    demo.shallow.strt(length=20).put()
    demo.shallow.sinebend(distance=100, offset=-200).put()
    # Pads
    pad1 = demo.pad_dc().put(ps.pin["c0"].move(300, 200, 0))
    demo.metaldc.sbend_p2p(ps.pin["c0"], Lstart=200).put()
    pad2 = demo.pad_dc().put(ps.pin["c1"].move(300, 100, 0))
    demo.metaldc.sbend_p2p(ps.pin["c1"], Lstart=200).put()
    # Lower arm
    demo.shallow.sinebend(distance=100, offset=40).put(0, -50)
    demo.shallow.strt(length=20).put()
    demo.shallow.sinebend(distance=100, offset=-40).put()
    demo.shallow.strt(length=300).put()
    demo.shallow.sinebend(distance=100, offset=-200).put()
    demo.shallow.strt(length=20).put()
    demo.shallow.sinebend(distance=100, offset=200).put()


qubit.put(0)
"""
qubit.put(740)
qubit2.put(1480)

qubit.put(0, -520)
qubit.put(740, -520)
qubit2.put(1480, -520)

qubit.put(0, -1040)
qubit.put(740, -1040)
qubit2.put(1480, -1040)

qubit.put(0, -1560)
qubit.put(740, -1560)
qubit2.put(1480, -1560)
"""
nd.export_gds()
