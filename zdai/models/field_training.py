# Copyright 2021 Zuva Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass
from typing import List


@dataclass
class DocumentType:
    classifications: List[str]
    percentage: float


@dataclass
class Language:
    language: str
    percentage: float


@dataclass
class Country:
    code: str
    name: str


@dataclass
class Jurisdiction:
    country: Country
    regions: List[str]


@dataclass
class FieldMetadata:
    field_id: str
    name: str
    description: str
    is_trained: bool
    read_only: bool
    file_ids: List[str]
    document_types: List[DocumentType]
    languages: List[Language]
    jurisdictions: List[Jurisdiction]
    tags: List[str]
    normalization_type: str


@dataclass
class FieldValidationLocation:
    character_start: int
    character_end: int


@dataclass
class FieldValidationDetails:
    file_id: str
    type: str
    location: FieldValidationLocation


@dataclass
class FieldAccuracy:
    precision: float
    recall: float
    f_score: float
    example_count: int
