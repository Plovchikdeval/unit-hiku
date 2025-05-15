__version__ = (2, 1, 2)
# change-log: !!GLOBAL UPDATE!! FIX MORE BUGS + UPDATE BOT AND API!

"""
888    d8P   .d8888b.  888    888     888b     d888  .d88888b.  8888888b.   .d8888b.  
888   d8P   d88P  Y88b 888    888     8888b   d8888 d88P" "Y88b 888  "Y88b d88P  Y88b 
888  d8P    Y88b.      888    888     88888b.d88888 888     888 888    888 Y88b.      
888d88K      "Y888b.   8888888888 d8b 888Y88888P888 888     888 888    888  "Y888b.   
8888888b        "Y88b. 888    888 Y8P 888 Y888P 888 888     888 888    888     "Y88b. 
888  Y88b         "888 888    888     888  Y8P  888 888     888 888    888       "888 
888   Y88b  Y88b  d88P 888    888 d8b 888   "   888 Y88b. .d88P 888  .d88P Y88b  d88P 
888    Y88b  "Y8888P"  888    888 Y8P 888       888  "Y88888P"  8888888P"   "Y8888P" 
                                                           
(C) 2025 t.me/kshmods
Licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
"""
# scope: hikka_only
# scope: hikka_min 1.3.3
# meta developer: @kshmods

import aiohttp
import html
import logging
import re
import inspect
import io
from telethon.tl.functions.contacts import UnblockRequest
from .. import utils, loader

logger = logging.getLogger("Hiku")

class HikuAPI:
    async def get_all_modules(self) -> list:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://unit-hiku.top/api/module/all') as response:
                return [await response.json()][0]

    async def get_module_by_id(self, id) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://unit-hiku.top/api/module/info/{id}') as response:
                return await response.json()

    async def get_module_raw(self, developer, module_name) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://unit-hiku.top/api/module/{developer}/{module_name}') as response:
                return {"content": await response.content.read(), "name": f"{module_name}.py"}

@loader.tds
class Hiku(loader.Module, HikuAPI):
    """Search modules!"""
    strings = {
        "name": "UnitHiku",
        "wait": "<emoji document_id=5787344001862471785>✍️</emoji> <b>Searching for {search_query} among {number_of_all_modules} modules...</b>",
        "found": "🎲 Current module: {current_index}/{count}\n"
                 "🔎 Found the module <b>{name}</b> by query: <b>{query}</b>"
                 "\n<b>ℹ️ Description:</b> {description}"
                 "\n<b>🧩 Developer:</b> @{username}"
                 "\n\n{commands}",
        "command_template": "{emoji} <code>{prefix}{command}</code> - {description}\n",
        "emojis": {
            1: "<emoji document_id=5449498872176983423>1️⃣</emoji>",
            2: "<emoji document_id=5447575603001705541>2️⃣</emoji>",
            3: "<emoji document_id=5447344971847844130>3️⃣</emoji>",
            4: "<emoji document_id=5449783211896879221>4️⃣</emoji>",
            5: "<emoji document_id=5449556257235024153>5️⃣</emoji>",
            6: "<emoji document_id=5449643483725837995>6️⃣</emoji>",
            7: "<emoji document_id=5447255791146910115>7️⃣</emoji>",
            8: "<emoji document_id=5449394534536462346>8️⃣</emoji>",
            9: "<emoji document_id=5447140424030371281>9️⃣</emoji>",
        },
        "404": "<emoji document_id=5019523782004441717>❌</emoji><b> Not found</b>",
        "noargs": "<emoji document_id=5019523782004441717>❌</emoji><b> Not args</b>",
        "no_info": "<emoji document_id=5019523782004441717>❌</emoji><b> Not found.</b>",
        "old_version": "<blockquote><emoji document_id=5875291072225087249>📊</emoji> You have old Hiku ({ver}) </b></blockquote>\n\n<blockquote><emoji document_id=5879883461711367869>⬇️</emoji> <b>New version: {new_ver} <b></blockquote>",
        "fetch_failed": "<blockquote><emoji document_id=5208663713539704322>👎</emoji> <b>Fetching data failed</b></blockquote>",
        "update_command": "\n\n<blockquote><emoji document_id=5877410604225924969>🔄</emoji> To update type:</b> <code> {prefix}dlm {upd_file}</code></blockquote>",
        "update_whats_new": "\n\n<blockquote><emoji document_id=5879785854284599288>ℹ️</emoji> <b>Changelog:</b><code>{whats_new}</code>\n\n</blockquote>",
        "actual_version": "<blockquote> <emoji document_id=5208763618773978162>✅</emoji>You have actual UnitHiku ({ver})</b></blockquote>",
        "join_channel": "The channel with all news UnitHiku!"
    }

    strings_ru = {
        "wait": "<emoji document_id=5787344001862471785>✍️</emoji> <b>Ищем {search_query} среди {number_of_all_modules} модулей...</b>",
        "found": "🎲 Кол-во найденных модулей: {count}\n"
                 "🔎 Найден модуль <b>{name}</b> по запросу: <b>{query}</b>"
                 "\n<b>ℹ️ Описание:</b> {description}"
                 "\n<b>🧩 Разработчик:</b> @{username}"
                 "\n\n{commands}",
        "command_template": "{emoji} <code>{prefix}{command}</code> - {description}\n",
        "emojis": {
            1: "<emoji document_id=5449498872176983423>1️⃣</emoji>",
            2: "<emoji document_id=5447575603001705541>2️⃣</emoji>",
            3: "<emoji document_id=5447344971847844130>3️⃣</emoji>",
            4: "<emoji document_id=5449783211896879221>4️⃣</emoji>",
            5: "<emoji document_id=5449556257235024153>5️⃣</emoji>",
            6: "<emoji document_id=5449643483725837995>6️⃣</emoji>",
            7: "<emoji document_id=5447255791146910115>7️⃣</emoji>",
            8: "<emoji document_id=5449394534536462346>8️⃣</emoji>",
            9: "<emoji document_id=5447140424030371281>9️⃣</emoji>",
        },
        "404": "<emoji document_id=5210952531676504517>❌</emoji> <b>Не найдено</b>",
        "noargs": "<emoji document_id=5210952531676504517>❌</emoji> <b>Нет аргументов</b>",
        "no_info": "<emoji document_id=5210952531676504517>❌</emoji> Нет информации.",
        "actual_version": "<blockquote> <emoji document_id=5208763618773978162>✅</emoji>У вас актуальная версия Hiku ({ver})</b></blockquote>",
        "old_version": "<blockquote><emoji document_id=5875291072225087249>📊</emoji> У вас устаревшая версия UnitHiku ({ver}) </b></blockquote>\n\n<blockquote><emoji document_id=5879883461711367869>⬇️</emoji> <b>Новая версия: {new_ver} <b></blockquote>",
        "update_command": "\n\n<blockquote><emoji document_id=5877410604225924969>🔄</emoji> Для обновления введите:</b> <code> {prefix}dlm {upd_file}</code></blockquote>",
        "update_whats_new": "\n\n<blockquote><emoji document_id=5879785854284599288>ℹ️</emoji> <b>Список изменений:</b><code>{whats_new}</code>\n\n</blockquote>",
        "fetch_failed": "<blockquote><emoji document_id=5208663713539704322>👎</emoji> <b>Не удалось получить данные</b></blockquote>",
        "join_channel": "Канал со всеми новостями UnitHiku!"
    }

    async def on_dlmod(self, client, db):
        try:
            await client(UnblockRequest("@unithiku_offbot"))
            await utils.dnd(self._client, "@unithiku_offbot", archive=True)
            await self._client.send_message(7844809113, f"/set_prefix {self.get_prefix()}")
        except:
            pass

    async def client_ready(self, client, db):
        self._prefix = self._client.loader.get_prefix()
        self.repo = "https://raw.githubusercontent.com/Plovchikdeval/unit-hiku/refs/heads/main/"
        try:
            await client(UnblockRequest("@unithiku_offbot"))
            await utils.dnd(self._client, "@unithiku_offbot", archive=True)
            await self._client.send_message('@unithiku_offbot', '/start')
            await self._client.send_message(7844809113, f"/set_prefix {self.get_prefix()}")
        except:
            pass

        await self.request_join(
            "@unithiku_updates",
            self.strings['join_channel'],
        )

    def __init__(self):
        self.BOT = 7844809113

    @loader.command()
    async def hikucmd(self, message):
        """[query] - Search module"""
        args = utils.get_args_raw(message)
        await utils.answer(message, self.strings["wait"].format(
            search_query=args,
            number_of_all_modules=len(await self.get_all_modules())
        ))
        if not args:
            return await utils.answer(message, self.strings["noargs"])

        modules = await self.get_all_modules()
        mods_to_show = []

        for module in modules:
            if (
                args.lower() in module['name'].lower() or
                args.lower() in module['description'].lower() or
                args.lower() in module['developer'].lower() or
                any(args in cmd or args in cmd_desc for func in module['commands'] for cmd, cmd_desc in func.items())
            ):
                mods_to_show.append(module)

        if not mods_to_show:
            return await utils.answer(message, self.strings('404'))

        await self._show_module(message, mods_to_show, 0)

    async def _show_module(self, message, mods_to_show, index):
        """Helper function to display a module with navigation buttons."""
        module = mods_to_show[index]

        commands = []
        command_count = 0
        for func in module["commands"]:
            for command, description in func.items():
                command_count += 1
                if command.endswith('cmd'):
                    command = command.replace('cmd', '')
                if command_count < 10:
                    commands.append(
                        self.strings["command_template"].format(
                            prefix=self._prefix,
                            command=html.escape(command),
                            emoji=self.strings['emojis'][command_count],
                            description=html.escape(description) if description else self.strings["no_info"]
                        )
                    )
                else:
                    commands.append("...")

        module_text = self.strings["found"].format(
            query=utils.get_args_raw(message),
            name=module['name'] if module['name'] else self.strings["no_info"],
            description=module['description'] if module['description'] else self.strings["no_info"],
            username=module['developer'],
            commands=''.join(commands),
            prefix=self._prefix,
            count=f'{len(mods_to_show)}',
            current_index=f'{index+1}',
        )

        markup = [
            [
                {
                    'text': f'⬇ Download',
                    'callback': self._inline_download,
                    'args': [f"https://unit-hiku.top/api/module/download/{module['id']}", module['id']]
                }
            ],
            []
        ]

        if index > 0:
            markup[1].append({
                'text': '◀ Back',
                'callback': self._prev_mod,
                'args': [mods_to_show, index - 1]
            })

        if index < len(mods_to_show) - 1:
            markup[1].append({
                'text': 'Next ▶',
                'callback': self._next_mod,
                'args': [mods_to_show, index + 1]
            })

        await utils.answer(message, module_text, reply_markup=markup)

    async def _prev_mod(self, call, mods_to_show, index):
        """Callback function to show the previous module."""
        await self._show_module(call, mods_to_show, index)

    async def _next_mod(self, call, mods_to_show, index):
        """Callback function to show the next module."""
        await self._show_module(call, mods_to_show, index)

    @loader.watcher(only_messages=True, startswith="#install", from_id=7703725985)
    async def download_module(self, message):
        match = re.search(r'#install:(\d+)', message.raw_text)
        if match:
            module_id = match.group(1)

        await message.delete()

        link = f"https://unit-hiku.top/api/module/download/{module_id}"

        await self._load_module(link)

    @loader.inline_handler()
    async def hiku(self, query):
        """[query] - Inline search modules"""

        if not query.args or not query.args.strip():
            return {
                "title": "No query",
                "description": "No args",
                "thumb": "https://img.icons8.com/?size=100&id=NIWYFnJlcBfr&format=png&color=000000",
                "message": "404 Not Found",
            }

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://unit-hiku.top/api/module/all") as response:
                all_modules = await response.json()

        mods_to_show = []
        query_lower = query.args.lower()

        for module in all_modules:
            module_name = module.get('name', '').lower()
            developer_name = module.get('developer', '').lower()
            commands = module.get('commands', [])

            if (query_lower in module_name or
                query_lower in developer_name or
                any(query_lower in cmd_key for cmd in commands for cmd_key in cmd.keys())):

                command_descriptions = []
                for index, cmd in enumerate(commands, start=1):
                    for cmd_key, cmd_desc in cmd.items():
                        emoji = self.strings["emojis"].get(index, "🔹")
                        if cmd_key.endswith('cmd'):
                            cmd_key = cmd_key.replace("cmd", "")
                        command_descriptions.append(
                            self.strings["command_template"].format(
                                emoji=emoji,
                                prefix=self._prefix,
                                command=utils.escape_html(cmd_key),
                                description=utils.escape_html(cmd_desc)
                            )
                        )

                formatted_commands = "".join(command_descriptions)

                mods_to_show.append({
                    "title": module.get('name', 'Unknown Module'),
                    "description": f"@{utils.escape_html(module.get('developer', 'Unknown developer'))}",
                    "photo": module.get("banner", ""),
                    "thumb": module.get(
                        "banner",
                        "https://img.icons8.com/?size=100&id=olDsW0G3zz22&format=png&color=000000",
                    ),
                    "message": self.strings["found"].format(
                        query=query.args,
                        name=module.get('name', self.strings["no_info"]),
                        description=module.get('description', self.strings["no_info"]),
                        username=module.get('developer', 'Unknown Developer'),
                        commands=formatted_commands,
                        prefix=self._prefix,
                        count='1',
                        current_index='1',
                    ),
                    "reply_markup": [
                        {
                            "text": "⬇️ Download",
                            "callback": self._inline_download,
                            "args": [f"https://unit-hiku.top/api/module/download/{module['id']}", module['id']]
                        }
                    ]
                })

        if len(mods_to_show) > 0:
            return mods_to_show
        elif len(mods_to_show) == 0:
            return {
                "title": "Not found",
                "description": "No module found",
                "thumb": "https://img.icons8.com/?size=100&id=NIWYFnJlcBfr&format=png&color=000000",
                "message": "404 Not Found",
            }

    @loader.watcher(only_messages=True, from_id=7844809113)
    async def remove_service_messages(self, message):
        if "#skipIfModuleInstalled" in message.raw_text:
            await message.delete()

    async def _load_module(self, url):
        loader_m = self.lookup("loader")
        await loader_m.download_and_install(url, None)

        if getattr(loader_m, "fully_loaded", False):
            loader_m.update_modules_in_db()

    async def _inline_download(self, call, url, module_id):
        await self._load_module(url)
        await self.client.send_message(self对待BOT, f"#download:{module_id}")

        info = await self.get_module_by_id(module_id)
        markup = [
            {
                "text": "❌ Close",
                "action": "close"
            }
        ]
        await call.edit(
            f"✔️ Module {info['name']} installed successfully\n\n<code>{self._client.loader.get_prefix()}help {info['name']}</code>\n\n<b><i>If module is not installed:</i></b>\n<code>{self._prefix}dlm {url}</code>",
            reply_markup=markup
        )

    @loader.command(en_doc="Check for updates", ru_doc="Проверить обновления", ua_doc="Перевірити оновлення")
    async def hcheck(self, message):
        """Check for updates"""
        module_name = self.strings('name')
        module = self.lookup(module_name)
        sys_module = inspect.getmodule(module)

        local_file = io.BytesIO(sys_module.__loader__.data)
        local_file.seek(0)
        local_first_line = local_file.readline().strip().decode("utf-8")

        correct_version = sys_module.__version__
        correct_version_str = ".".join(map(str, correct_version))

        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.repo}unit-hiku.py") as response:
                if response.status == 200:
                    remote_content = await response.text()
                    remote_lines = remote_content.splitlines()
                    what_new = remote_lines[1].split(":", 1)[1].strip() if len(remote_lines) > 2 and remote_lines[1].startswith("# change-log:") else ""
                    new_version = remote_lines[0].split("=", 1)[1].strip().strip("()").replace(",", "").replace(" ", ".")
                    new_version_tuple = tuple(map(int, new_version.split(".")))
                    if new_version_tuple <= __version__:
                        await utils.answer(message, self.strings("actual_version").format(ver=correct_version_str))
                        return
                else:
                    await utils.answer(message, self.strings("fetch_failed"))
                    return

        if local_first_line.replace(" ", "") == remote_lines[0].strip().replace(" ", ""):
            await utils.answer(message, self.strings("actual_version").format(ver=correct_version_str))
        else:
            update_message = self.strings("old_version").format(ver=correct_version_str, new_ver=new_version)
            update_message += self.strings("update_command").format(prefix=self._prefix, upd_file=f"{self.repo}/unit-hiku.py")
            if what_new:
                update_message += self.strings("update_whats_new").format(whats_new=what_new)
            await utils.answer(message, update_message)


    @loader.command()
    async def profile(self, message):
        """Your profile unit-hiku"""
        profile = await self.client.inline_query("unithiku_offbot", "profile")
        if profile:
        	chat_id = message.chat_id
        	await profile[0].click(chat_id)
        else:
        	await utils.answer(message, "😭Произошла ошибка при открытии профиля")
        
    @loader.command()
    async def serverinfo(self, message):
        """Server statistics unit-hiku"""
        profile = await self.client.inline_query("unithiku_offbot", "si")
        if profile:
        	chat_id = message.chat_id
        	await profile[0].click(chat_id)
        else:
        	await utils.answer(message, "😭Произошла ошибка при открытии статистики сервера")