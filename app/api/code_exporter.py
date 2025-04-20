from sqlalchemy.orm import Session
from app import crud


def generate_screen_code(db: Session, screen_id: int) -> str:
    screen = crud.screen.get(db, id=screen_id)
    if not screen:
        return ""
    instances = crud.componentinstance.get_multi_by_screen(db, screen_id=screen_id)
    # Basic React Native component code
    safe_name = ''.join(ch for ch in screen.name.title() if ch.isalnum())
    lines = [
        f"// Generated code for screen: {screen.name}",
        "import React from 'react';",
        "import { View, Text } from 'react-native';",
        "",
        f"const {safe_name}Screen = () => (",
        "  <View style={{ flex: 1, padding: 16 }}>",
    ]
    for inst in instances:
        if inst.component_type == 'Text':
            text = inst.props.get('text', f'Text #{inst.id}')
            lines.append(f"    <Text key=\"{inst.id}\">{text}</Text>")
        else:
            lines.append(f"    <View key=\"{inst.id}\" />  /* {inst.component_type} */")
    lines.extend([
        "  </View>",
        ");",
        "",
        f"export default {safe_name}Screen;",
    ])
    return "\n".join(lines)
