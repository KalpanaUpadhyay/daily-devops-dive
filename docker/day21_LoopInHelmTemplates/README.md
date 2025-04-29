🎯 Goal for Today:
Make Helm charts configurable using values.yaml + if, range, and with in templates.

🧠 Key Helm Template Features
Helm templates use Go templating language ({{ }}) to control rendering.

1. ✅ if – Conditional Resource Rendering
# templates/ingress.yaml
{{- if .Values.ingress.enabled }}
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {{ .Release.Name }}-ingress
spec:
  ...
{{- end }}
values.yaml:

ingress:
  enabled: true
🔁 Set enabled: false to skip creating Ingress.

2. 🔁 range – Loop Over a List or Map
# templates/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
data:
{{- range $key, $val := .Values.config }}
  {{ $key }}: "{{ $val }}"
{{- end }}

values.yaml:

config:
  DB_HOST: localhost
  DB_PORT: "5432"
🔁 Generates:

data:
  DB_HOST: "localhost"
  DB_PORT: "5432"

3. 🧩 with – Simplifies Nested Access

# templates/deployment.yaml
{{- with .Values.resources }}
resources:
  limits:
    cpu: {{ .cpu }}
    memory: {{ .memory }}
{{- end }}

values.yaml:

resources:
  cpu: 500m
  memory: 256Mi

🔁 with reduces .Values.resources.cpu to just .cpu inside the block.

4. 🌟 Combine Them!
{{- if .Values.env.enabled }}
env:
{{- range $k, $v := .Values.env.vars }}
  - name: {{ $k }}
    value: "{{ $v }}"
{{- end }}
{{- end }}

values.yaml:
env:
  enabled: true
  vars:
    ENV: production
    DEBUG: "false"

🛠️ Real Use Case
You can use this to make charts that:

Only create resources if needed

Add optional configuration

Dynamically render labels, ports, or volumes

✅ Today You Learned:

Feature	Purpose
if	Conditionally render blocks
range	Loop over lists/maps
with	Simplify access to nested fields
💡 These make your Helm charts flexible, scalable, and production-grade.
