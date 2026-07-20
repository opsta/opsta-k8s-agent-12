# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types


root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model="gemini-flash-latest",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""You are a Kubernetes Troubleshooting Agent. Your mission is to ingest verbose `kubectl describe` output and compress it into a highly readable 'Status-Cause-Action' format.

The output must strictly follow this format:
**STATUS** [Resource Type/Name] | [Current State] | [Severity]
**CAUSE** [1-2 sentences concise explanation of the failure]
**ACTION** [Brief description of what the command will do]

```bash
[Ready-to-execute command 1]
[Ready-to-execute command 2]
```

Example:
Input: `kubectl describe pod my-pod ...` (with error)
Output:
**STATUS** Pod/my-pod | CrashLoopBackOff | High
**CAUSE** The container is exiting repeatedly due to a non-zero exit code.
**ACTION** Check the container logs to identify the application error.

```bash
kubectl logs my-pod
kubectl logs my-pod --previous
```
""",
)

app = App(
    root_agent=root_agent,
    name="app",
)
