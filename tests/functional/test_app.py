"""
   Copyright 2023 Flexport International, LLC

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import json

from rock_paper_scissors.app import app


def test_rps():
    """
    Test Flask Application and API for Rock Paper Scissors
    """

    with app.test_client() as test_client:
        response = test_client.post(
            "/rps", data=json.dumps({"move": "Rock"}), content_type="application/json"
        )
        assert response.status_code == 200

    with app.test_client() as test_client:
        response = test_client.get("/health")
        assert response.status_code == 200

    with app.test_client() as test_client:
        response = test_client.post(
            "/rps", data=json.dumps({}), content_type="application/json"
        )
        assert response.status_code == 500

    with app.test_client() as test_client:
        response = test_client.post(
            "/rps",
            data=json.dumps({"move": "Rock"}),
            content_type="application/json",
        )
        assert response.status_code == 200
    with app.test_client() as test_client:
        response = test_client.post(
            "/rps",
            data=json.dumps({"move": "Rock"}),
            content_type="application/json",
        )
        assert response.status_code == 200
    
    