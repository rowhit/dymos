from __future__ import print_function, absolute_import, division

import unittest

import matplotlib
matplotlib.use('Agg')

from openmdao.utils.assert_utils import assert_rel_error

from dymos.examples.aircraft_steady_flight.ex_aircraft_steady_flight import \
    ex_aircraft_steady_flight


class TestExSteadyAircraftFlight(unittest.TestCase):

    def test_ex_aircraft_steady_flight(self):
        p = ex_aircraft_steady_flight(optimizer='SLSQP', transcription='radau-ps')
        phase = p.model.phase0

        assert_rel_error(self, phase.get_values('range', units='NM')[-1], 726.7, tolerance=1.0E-2)


if __name__ == '__main__':
    unittest.main()
