FROM phelsong/archpy:latest

WORKDIR /opt/joshsw.dev
COPY . /opt/joshsw.dev

USER root
RUN chown -R runner:runner /opt/joshsw.dev
RUN chmod -R 550 /opt/joshsw.dev

EXPOSE 8062

USER runner
# RUN bash -c "poetry install"
CMD [ "bash", "-c", "poetry install; poetry run start" ]
