# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
<<<<<<<< HEAD:tests/system/providers/google/cloud/gcs/resources/transform_script.py
from __future__ import annotations

import sys

source = sys.argv[1]
destination = sys.argv[2]

print("Running script")
with open(source) as src, open(destination, "w+") as dest:
    lines = [line.upper() for line in src.readlines()]
    print(lines)
    dest.writelines(lines)
========
>>>>>>>> 6bc4b41286 (refactor: add socar revision):airflow/providers/alibaba/cloud/log/__init__.py~merged
