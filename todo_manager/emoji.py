# Custom emoji's as variables to enhance CLI and user visuals

import todo_manager.emoji as emoji

emoji_add_task = emoji.emojize(":heavy_plus_sign:")  # ➕
emoji_delete_task = emoji.emojize(":wastebasket:")   # 🗑️
emoji_list_task = emoji.emojize(":memo:")            # 📝
emoji_quit = emoji.emojize(":waving_hand:")          # 👋
emoji_complete_task = emoji.emojize(":check_mark:")  # ✅
emoji_edit_task = emoji.emojize(":pencil:")          # ✏️
emoji_priority_high = emoji.emojize(":exclamation:") # ❗
emoji_not_found = emoji.emojize(":cross_mark:")  # ❌
emoji_wink_face = emoji.emojize(":winking_face:")  # 😉