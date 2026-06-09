from amaranth.build import *

from .ice40 import *


__all__ = ["GlasgowRevD0Platform"]


class _GlasgowRevDPlatform(GlasgowECP5Platform):
    device      = "TODO"
    package     = "BG256"
    default_clk = "clk_if"
    resources   = [
        Resource("clk_fx", 0, Pins("C8", dir="i"),
                 Clock(48e6), Attrs(GLOBAL="1", IO_STANDARD="SB_LVCMOS")),
        Resource("clk_if", 0, Pins("E8", dir="i"),
                 Clock(48e6), Attrs(GLOBAL="1", IO_STANDARD="SB_LVCMOS")),

        Resource("fx2", 0,
            Subsignal("sloe",    Pins("B5", dir="o")),
            Subsignal("slrd",    Pins("E9", dir="o")),
            Subsignal("slwr",    Pins("D10", dir="o")),
            Subsignal("pktend",  Pins("E11", dir="o")),
            Subsignal("fifoadr", Pins("D9 D8", dir="o")),
            Subsignal("flag",    Pins("B10 E10 A9 E4", dir="i")),
            Subsignal("fd",      Pins("T8 T7 M7 N7 P7 R7 R6 T6", dir="io")),
            Attrs(IO_STANDARD="SB_LVCMOS")
        ),

        Resource("i2c", 0,
            Subsignal("scl", Pins("A12", dir="io")),
            Subsignal("sda", Pins("D11", dir="io")),
            Attrs(IO_STANDARD="SB_LVCMOS")
        ),

        Resource("alert", 0, PinsN("B4", dir="oe"), Attrs(IO_STANDARD="SB_LVCMOS")),

        Resource("led", 0, Pins("D13", dir="o"), Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("led", 1, Pins("E13", dir="o"), Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("led", 2, Pins("A13", dir="o"), Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("led", 3, Pins("A14", dir="o"), Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("led", 4, Pins("B14", dir="o"), Attrs(IO_STANDARD="SB_LVCMOS")),

        Resource("port_a", 0,
                 Subsignal("io", Pins("B2"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("B1", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_a", 1,
                 Subsignal("io", Pins("D3"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("C3", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_a", 2,
                 Subsignal("io", Pins("C2"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("C1", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_a", 3,
                 Subsignal("io", Pins("F3"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("E3", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_a", 4,
                 Subsignal("io", Pins("E2"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("D1", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_a", 5,
                 Subsignal("io", Pins("F5"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("F4", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_a", 6,
                 Subsignal("io", Pins("G5"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("G4", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_a", 7,
                 Subsignal("io", Pins("E1"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("F2", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),

        Resource("port_b", 0,
                 Subsignal("io", Pins("G2"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("F1",  dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_b", 1,
                 Subsignal("io", Pins("H3"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("G3", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_b", 2,
                 Subsignal("io", Pins("H4"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("H5", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_b", 3,
                 Subsignal("io", Pins("J5"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("J4", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_b", 4,
                 Subsignal("io", Pins("H2"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("G1", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_b", 5,
                 Subsignal("io", Pins("K3"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("J3", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_b", 6,
                 Subsignal("io", Pins("J2"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("J1", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_b", 7,
                 Subsignal("io", Pins("K2"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("K1", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),

        Resource("port_c", 0,
                 Subsignal("io", Pins("B16"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("B15",  dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_c", 1,
                 Subsignal("io", Pins("C14"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("D14", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_c", 2,
                 Subsignal("io", Pins("C16"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("C15", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_c", 3,
                 Subsignal("io", Pins("E14"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("F14", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_c", 4,
                 Subsignal("io", Pins("D16"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("E15", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_c", 5,
                 Subsignal("io", Pins("F13"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("F12", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_c", 6,
                 Subsignal("io", Pins("G12"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("G13", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_c", 7,
                 Subsignal("io", Pins("F15"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("E16", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),

        Resource("port_d", 0,
                 Subsignal("io", Pins("F16"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("G15",  dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_d", 1,
                 Subsignal("io", Pins("G14"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("H14", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_d", 2,
                 Subsignal("io", Pins("H12"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("H13", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_d", 3,
                 Subsignal("io", Pins("J13"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("J12", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_d", 4,
                 Subsignal("io", Pins("G16"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("H15", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_d", 5,
                 Subsignal("io", Pins("J14"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("K14", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_d", 6,
                 Subsignal("io", Pins("J16"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("J15", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("port_d", 7,
                 Subsignal("io", Pins("K16"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("K15", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),

        Resource("aux", 0, Pins("A10"), Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("aux", 1, Pins("C9"),  Attrs(IO_STANDARD="SB_LVCMOS")),

        # TODO: unused pins are tied to ground, do we need to specify something?
        Resource("unused", 0, Pins("B8 B9 A10 C10 B11 C11 A11 B12 C12 D12 E12 A6 E6 D6 C6 B6 E7 D7 "
                                   "C7 B7 A7 R8 P8 M9", dir="io"), Attrs(IO_STANDARD="SB_LVCMOS")),
    ]
    # TODO: new LVDS pinout
    connectors  = [
        #                     1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22
        #                     23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44
        Connector("lvds", 0, "-  -  K1 -  J1 -  -  K2 H1 J2 H2 -  -  H3 G1 G3 G2 -  -  F3 F1 F4 "
                             "F2 -  -  E3 E1 E2 D1 -  -  D2 C1 D3 C2 -  -  C3 B1 C4 B2 -  -  -  "),
    ]

    # TODO: NAFE, RAM

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._init_glasgow_pins(
            ("A", "port_a", range(8)),
            ("B", "port_b", range(8)),
            ("C", "port_a", range(8)),
            ("D", "port_b", range(8)),
            ("S", "port_s", range(1)),
        )


class GlasgowRevD0Platform(_GlasgowRevCPlatform):
    resources = _GlasgowRevCPlatform.resources + [
        Resource("port_s", 0,
                 Subsignal("io", Pins("B13"), Attrs(PULLUP=1)),
                 Subsignal("oe", Pins("C13", dir="o")),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
    ]
