from django.core.management.commands.runserver import Command as BaseCommand


class Command(BaseCommand):
    def run(self, **options):
        warning_prefix = "WARNING: This is a development server."
        original_stdout_write = self.stdout.write
        original_stderr_write = self.stderr.write

        def filtered_write(msg="", style_func=None, ending=None):
            text = msg if isinstance(msg, str) else str(msg)
            if text.startswith(warning_prefix):
                return None
            return original_stdout_write(msg, style_func=style_func, ending=ending)

        def filtered_err_write(msg="", style_func=None, ending=None):
            text = msg if isinstance(msg, str) else str(msg)
            if text.startswith(warning_prefix):
                return None
            return original_stderr_write(msg, style_func=style_func, ending=ending)

        self.stdout.write = filtered_write
        self.stderr.write = filtered_err_write
        return super().run(**options)
