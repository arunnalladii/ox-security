# !/usr/bin/env python3
"""
Unit tests for CLOUDFORMATION linter cfn-lint
This class has been automatically @generated by .automation/build.py, please don't update it manually
"""

from unittest import TestCase

from megalinter.tests.test_megalinter.LinterTestRoot import LinterTestRoot


class cloudformation_cfn_lint_test(TestCase, LinterTestRoot):
    descriptor_id = "CLOUDFORMATION"
    linter_name = "cfn-lint"
