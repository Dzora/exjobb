# Week 15, 27-04-2020 - 01-05-2020
## Done
Got Prometheus and Grafana working in my cluster and found JMeter for stresstesting. Also updated the TeaStore to be able to use no tracing at all.
## Problems
JMeter behaves oddly when used outside the cluster. The results for the first test was garbage.
## Do
Deploy JMeter inside the cluster to encapsulate the testbed and run the tests again.