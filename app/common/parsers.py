import json
from pydantic import BaseModel


class ResponseParser:
    @staticmethod
    def parse_response(
        response_json: str, schema_type: BaseModel
    ) -> dict[str, BaseModel]:
        try:
            response_data = json.loads(response_json)
        except json.JSONDecodeError as e:
            print("Malformed JSON data:", e)
            raise

        parsed_data = {}

        for section_name, section_data in response_data.items():
            if isinstance(section_data, dict):
                section_response = schema_type(**section_data)
                parsed_data[section_name] = section_response

        if not parsed_data:
            section_response = schema_type(**response_data)
            return section_response
        else:
            return parsed_data
