🧠 What You’ll Learn:
How to scale a stateful application (Cassandra)

How Kubernetes StatefulSets manage identity and storage

How scaling works differently from stateless apps

🛠️ Steps:
1. Check Current StatefulSet Replicas
kubectl get statefulsets

You should see something like:
NAME        READY   AGE
cassandra   1/1     1d

2. Scale Cassandra Up to 3 Pods
kubectl scale statefulset cassandra --replicas=3

This will add more Cassandra pods with names like:
cassandra-0
cassandra-1
cassandra-2

3. Watch Pods Come Up
kubectl get pods -l app.kubernetes.io/name=cassandra -w

It may take some time. Kubernetes creates each pod sequentially in a StatefulSet.

4. Verify Cluster Size (Inside Pod)
kubectl exec -it cassandra-0 -- cqlsh

Then run:
DESCRIBE CLUSTER;

You should see 3 nodes in the cluster now.

5. (Optional) Scale Down
You can also scale back down if you want:
kubectl scale statefulset cassandra --replicas=1

Note: Data volumes for cassandra-1 and cassandra-2 won’t be deleted unless you manually delete PVCs (Persistent Volume Claim).

📌 Notes:

Scaling StatefulSets is stateful, so each pod keeps its identity (hostname, storage).

Cassandra automatically joins new nodes into the cluster if configured right (Bitnami Helm handles this for you).


