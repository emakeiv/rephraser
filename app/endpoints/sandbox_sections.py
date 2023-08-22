
 body = request.dict()
    print(body.get('description'))
    tasks = []
    for section in body.get('sections').items():
        section_name, section_data = section
        for section in section_data.items():
            subject, variant = section
            if variant:
                tasks.append(openai_client.get_response(body.get('description'), variant, template_name="generate_section_template", subject=subject))

    generated_responses = await asyncio.gather(*tasks)
    print(generated_responses)
