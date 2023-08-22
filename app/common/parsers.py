import json
from pydantic import BaseModel

class ResponseParser:

    @staticmethod
    def parse_response(response_json: str, schema_type: BaseModel) -> dict[str, BaseModel]:
        try:
            response_data = json.loads(response_json)
        except json.JSONDecodeError as e:
            print("Malformed JSON data:", e)
            raise
        
        parsed_data = {}
        for section_name, section_data in response_data.items():
            section_response_list = []
            if isinstance(section_data, list):
                for section_entry in section_data:
                    section_response = schema_type(**section_entry)
                    section_response_list.append(section_response)
            else:
                section_response = schema_type(**section_data)
                section_response_list.append(section_response)
            
            parsed_data[section_name] = section_response_list
        
        return parsed_data
