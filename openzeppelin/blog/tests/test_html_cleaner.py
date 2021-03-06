import unittest

import testscenarios

import html_cleaner


class TestHTMLCleaner(testscenarios.WithScenarios, unittest.TestCase):

    scenarios = [
        ('noop with target different than blank from links', dict(
            html_input='<a target="test">dummy</a>',
            expected_output='<a target="test">dummy</a>')),
        ('remove target blank from links', dict(
            html_input='<a target="_blank">dummy</a>',
            expected_output='<a>dummy</a>')),
        ('remove rel from links', dict(
            html_input='<a rel="dummy">dummy</a>',
            expected_output='<a>dummy</a>')),
        ('remove data-href from links', dict(
            html_input='<a data-href="dummy">dummy</a>',
            expected_output='<a>dummy</a>')),
        ('remove class-graf', dict(
            html_input='<p class="graf graf--p graf-after--p">dummy</p>',
            expected_output='<p>dummy</p>')),
        ('remove class graf in h3', dict(
            html_input='<h3 class="graf graf--h3 graf-after--p">dummy</h3>',
            expected_output='<h3>dummy</h3>')),
    ]

    def test_clean(self):
        self.assertEqual(
            html_cleaner.clean(self.html_input),
            self.expected_output)
