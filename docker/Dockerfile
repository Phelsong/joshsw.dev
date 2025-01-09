FROM phelsong/archpy:latest

WORKDIR /opt/joshsw.dev
COPY . /opt/joshsw.dev
# COPY ./pyproject.toml /opt/joshsw.dev
# COPY ./poetry.lock /opt/joshsw.dev

USER root
RUN chown -R runner:runner /opt/joshsw.dev
RUN chmod -R 550 /opt/joshsw.dev
RUN chmod 600 /opt/joshsw.dev/poetry.lock

EXPOSE 8062

USER runner
SHELL [ "/bin/bash"]
CMD [ "./start.sh" ]
