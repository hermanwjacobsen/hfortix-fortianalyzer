"""
FortiAnalyzer API endpoint: sys.login.challenge

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SysLoginChallenge:
    """
    FortiAnalyzer endpoint: sys.login.challenge
    
    
    Available methods: exec
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def exec(self, answer: str | None = None, session: str | None = None) -> FortiAnalyzerResponse:
        """
        EXEC operation.
        
        Args:
            answer: Answer to the challenge question from previous request.
            session: Session ID returned from <a href="#login_user">login/user</a> or previous <a href="#login_challenge">login/challenge</a> command.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/sys/login/challenge"
        
        # Build data payload
        data = {}
        if answer is not None:
            data["answer"] = answer
        if session is not None:
            data["session"] = session
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="exec",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)
