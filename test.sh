#!/bin/bash

echo "Running portfolio tests..."
python3 -m tests.test_portfolio

echo "Running performance tests..."
python3 -m tests.test_performance

echo "Running risk tests..."
python3 -m tests.test_risk

echo "Running report tests..."
python3 -m tests.test_report

echo "All tests passed!"
