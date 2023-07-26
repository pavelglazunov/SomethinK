# import os
#
# MODAL_INIT_FILE = """
# =====modal_imports=====
# """
#
# MODALS_REPLACEMENT = {
#
# }
#
#
# def mg_modals_input(_key: list) -> str:
#     result = ""
#     print(">>>>>>>>>>>>>>>", os.getcwd())
#     for i in ("embed_modals", "feedback_modals", "report_modals"):
#         if os.path.isfile(f"{i}.py"):
#             result += f"from . import {i} \n"
#     """
#     from . import embed_modals
#     from . import feedback_modals
#     from . import report_modals
#
#     """
#
#     return result
#
#
# MODALS_REPLACEMENT_WITH_GENERATE_DATA = {
#     "=====modal_imports=====": mg_modals_input
# }
